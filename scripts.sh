docker build -t smart_stats_loader:latest --build-arg service=loader .

docker rm -f smart_stats_loader || true

docker run --name smart_stats_loader -e HOST="http://host.docker.internal" -p 9998:8000 smart_stats_loader:latest


#mcp_server

docker build -t smart_stats_mcp_server:latest --build-arg service=mcp_server .

docker run -p 9999:8000 --name smart_stats_mcp_server smart_stats_mcp_server:latest


#test
docker build -t smart_stats_test:latest --build-arg service=test .

docker run --name smart_stats_test smart_stats_test:latest


npx @modelcontextprotocol/inspector