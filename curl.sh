# For json data:
curl -H "Content-Type: application/json" --data @data.json http://127.0.0.1:8080/predictions/vbr

# For text file data:
# curl -X POST -F "file=data.txt" http://127.0.0.1:8080/predictions/vbr

