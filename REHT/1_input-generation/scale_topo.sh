#!/usr/bin/env bash 

# input .gro file
gro=$1

# number of replicas
nrep=32

# effective scaled atoms temperature range
tmin=300
tmax=600

# build geometric progression
list=$(
awk -v n=$nrep \
    -v tmin=$tmin \
    -v tmax=$tmax \
  'BEGIN{for(i=0;i<n;i++){
    t=tmin*exp(i*log(tmax/tmin)/(n-1));
    printf(t); if(i<n-1)printf(",");
  }
}'
)
echo $list 

for((i=0;i<nrep;i++))
do

      # choose lambda as T[0]/T[i]
      # high temperature = low lambda
      lambda=$(echo $list | awk 'BEGIN{FS=",";}{print $1/$'$((i+1))';}')
      echo $lambda

      # samu 12.11.24 check
      temp=$(echo $list | awk 'BEGIN{FS=",";}{print $(('$i'+1));}')
      echo Replica ${i} at T = ${temp} with lambda = ${lambda}

      # process topology
      plumed partial_tempering $lambda < processed_.top > md$i.top

      # prepare tpr file
      gmx grompp  -maxwarn 1 -o 1md$i.tpr -f md$i.mdp -p md$i.top -c ${gro} -n index.ndx 
done
