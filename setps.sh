docker create --driver bridge micro-network

docker build -t userapi .
docker build -t bookapi .
docker build -t orderapi .
docker build -t frontendapi .

docker run -p 5001:5001 --detach --name user-service-c --net=micro_network userapi
docker run -p 5002:5002 --detach --name book-service-c --net=micro_network bookapi
docker run -p 5003:5003 --detach --name order-service-c --net=micro_network orderapi
docker run -p 5000:5000 --detach --name frontend-service-c --net=micro_network frontendapi
