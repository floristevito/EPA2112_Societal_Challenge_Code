FROM node:14.18

RUN mkdir -p /srv/app/qr
WORKDIR /srv/app/qr

COPY package.json /srv/app/qr
COPY package-lock.json /srv/app/qr

RUN npm install 

COPY . /srv/app/reporting

CMD ["npm", "run", "serve"]