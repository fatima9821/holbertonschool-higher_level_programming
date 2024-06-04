#utilisation de l'image alpine comme base
FROM alpine:lastest

# instalation le package curl
RUN apk add --no-cache curl

#copier le fichier de config dans le conteneur
COPY config.txt /app/config.txt
