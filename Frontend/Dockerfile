FROM node:20-alpine as base

WORKDIR /web

COPY . /web

RUN npm install

RUN npm run build

EXPOSE 5001

CMD npm run dev -- --host 0.0.0.0