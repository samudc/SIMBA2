#!/usr/bin/env bash 

# number of replicas
nrep=32
# effective system temperature range
tmin=300
tmax=340

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

cp sample.mdp md0.mdp 

for temp in ${list//,/ }
do
	echo Replica ${i} at T = ${temp} 
	cp sample.mdp md${i}.mdp 
	perl -i -pes/"XXX"/"${temp}"/g md${i}.mdp 
	i=$(($i+1));
done

cp md.mdp md0.mdp 
