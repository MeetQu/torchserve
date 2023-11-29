# TorchServe Practice

For detailed README file, please see anthoer repository [TorchServe Deployment](https://github.com/sudrizzz/vbr#6-torchserve-%E9%83%A8%E7%BD%B2) (simplified Chinese only).

## Getting Started

https://pytorch.org/serve/getting_started.html

## Run

### Script Model File

1. Put script model under root folder of project, then the project structure will be like:

```text
.  
├── script_model.pt     <--- torch script model file  
├── config.properties  
├── curl.sh  
├── data.json  
├── handler.py  
├── index_to_name.json  
├── restart.sh  
└── stop.sh  
```

### Edit configurations

1. Edit `restart.sh`, modify the project root path in line 1 and modify the conda activate path in line 2;
2. Edit `curl.sh`, modify the service request url and choose the right method to send request;
3. Edit `data.json`;
4. Edit `handler.py` to process request data and prediction result;
5. Edit `index_to_name.json`, mapping index and class name;

### Start service

Give execute permission to the `.sh` files:

```shell
chmod +x restart.sh curl.sh stop.sh
```

1. Execute `restart.sh` to start torchserve service;
2. Execute `curl.sh` to test torchserve service;
3. Execute `stop.sh` to stop torchserve service;
