alias python=python3.8



python3.8 -m pip install cython==0.29.36 numpy
python3.8 -m pip install sparse_dot_topn==0.3.1 --no-cache-dir --no-build-isolation
python3.8 -m pip install sparse-dot-topn-for-blocks --no-cache-dir --no-build-isolation




sudo setfacl -m user:$USER:rw /var/run/docker.sock

docker build -t test/py38 .
docker run --name test -td docker.io/test/py38
docker exec -it 5f4ca2e7eaa7 bash
docker run -v /media/unman/data/marble:/home/risk -td test/py38e:live