FROM nginx:alpine

RUN apk update && apk add nano

COPY ./default.conf /etc/nginx/conf.d/

# copy user:foo password:bar
COPY ./.htpasswd /etc/nginx/

COPY ./cert.crt ./key.key /etc/nginx/cert/
