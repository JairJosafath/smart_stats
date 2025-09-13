#loader
docker build -t smart_stats_loader:latest --build-arg service=loader .

docker rm -f smart_stats_loader || true

docker run --name smart_stats_loader -d -e HOST="http://host.docker.internal" -p 9998:8000 smart_stats_loader:latest


#mcp_server
docker build -t smart_stats_mcp_server:latest --build-arg service=mcp_server .

docker rm -f smart_stats_mcp_server || true

docker run -d -p 9999:8000 --name smart_stats_mcp_server smart_stats_mcp_server:latest


#extractor
docker build -t smart_stats_extractor:latest --build-arg service=extractor .

docker rm -f smart_stats_extractor || true

docker run --name smart_stats_extractor -d -e HOST="http://host.docker.internal" -p 9997:8000 smart_stats_extractor:latest


#smart_stats
docker build -t smart_stats:latest --build-arg service=smart_stats .

docker rm -f smart_stats || true

docker run --name smart_stats -d -e HOST="http://host.docker.internal" -p 8000:8000 smart_stats:latest

