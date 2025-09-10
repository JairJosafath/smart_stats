docker build -t smart_stats_loader:latest --build-arg service=loader .

docker run --name smart_stats_loader smart_stats_loader:latest


#mcp_server

docker build -t smart_stats_mcp_server:latest --build-arg service=mcp_server .

docker run -p 9999:8000 --name smart_stats_mcp_server smart_stats_mcp_server:latest


#test
docker build -t smart_stats_test:latest --build-arg service=test .

docker run --name smart_stats_test smart_stats_test:latest


npx @modelcontextprotocol/inspector