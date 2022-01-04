FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=username
ENV POSTGRES_DB=owlappdb
COPY owlappdbcreate.sql /docker-entrypoint-initdb.d/owlappdbcreate.sql
