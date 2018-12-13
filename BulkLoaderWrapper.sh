#!/bin/bash
arangoimp --on-duplicate ignore \
	--log.level warn \
	--server.endpoint http+tcp://10.1.20.6:8529 \
	--server.authentication 'true' \
	--server.username root \
	--server.password openSesame \
	--server.database MelbourneDEM \
	--type csv \
	--create-collection true \
	--file nodes.csv \
	--collection people

arangoimp --on-duplicate ignore \
	--log.level warn \
	--server.endpoint http+tcp://10.1.20.6:8529 \
	--server.authentication 'true' \
	--server.username root \
	--server.password openSesame \
	--server.database MelbourneDEM \
	--type csv \
	--create-collection true \
	--create-collection-type edge \
	--file edges.csv \
	--collection people_links
