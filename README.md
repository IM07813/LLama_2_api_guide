# LLama_2_api_guide
running llama api through your terminal using replicate  

Steps to follow: 
step 1:

first download a virtual environment if you haven't already 
you can download it using pip on linux ubuntu 
<sudo apt install python3.11-venv>

step 2: 
create a new virtual environment:
<python3 -m venv myenv> where myenv == "you virtual env name" 
for example: 

my virtual env is llama2_api
so, my command will be <python3 -m venv llama2_api>


step 3:
activate your environment: 
source llama2_api/bin/activate 

the above command will activate your environment 
![Screenshot from 2024-02-08 02-13-28](https://github.com/IM07813/LLama_2_api_guide/assets/119739278/dcee8464-9061-41c6-9b72-ef4db3ae3742)

step 4:
download replicate inside your environment 
pip install replicate

The above command will install replicate inside your llama2_api venv 

step 5:

Next, copy your API token and authenticate by setting it as an environment variable:

export REPLICATE_API_TOKEN=r8_UCY********************************** (you can get your token from replicate link "https://replicate.com/account/api-tokens"
![Screenshot from 2024-02-08 02-15-04](https://github.com/IM07813/LLama_2_api_guide/assets/119739278/7f41ca7a-1b83-46f3-ba62-d3c3d89cc371)

step 6: 
make a directory inside your current directory:
for linux: 
mkdir llama2_api 
cd llama2_api 

step 7: 
copy paste the replit_python.py inside this llama2_api dirctory 

step 8: 
run the replit_python.py by typing python3 replit_python.py "your prompt" <seed> 

for example: 
to run the prompt "how are you" with <seed> as 123 

you have to run the following command: 

python3 replit_python.py "how are you" 123 

output for this will be: 
![Screenshot from 2024-02-08 02-17-31](https://github.com/IM07813/LLama_2_api_guide/assets/119739278/8cd14d61-a7a6-4bba-962f-5ca67621f74a)








