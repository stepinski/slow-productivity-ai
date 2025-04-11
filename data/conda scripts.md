create env

conda create -n dl2 python=3.7    
conda activate dl2            
conda install pytorch torchvision cpuonly -c pytorch
conda install -c anaconda scikit-learn
conda install scikit-learn-intelex
conda install matplotlib
conda install tqdm 

(example $ python -m sklearnex my_application.py)
