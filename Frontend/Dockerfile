FROM node:20.3.1-alpine as base

WORKDIR /web

COPY . .

RUN npm install -g npm
RUN npm install --save-dev --ignore-scripts

RUN npm run build

EXPOSE 5001

CMD npm run dev -- --host 0.0.0.0 --port 5001