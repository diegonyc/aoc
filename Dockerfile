FROM alpine:latest

RUN mkdir /opt/OrgFiles

WORKDIR /opt/OrgFiles

RUN apk add emacs-nox
RUN apk add python3
RUN apk add clojure --repository=https://dl-cdn.alpinelinux.org/alpine/edge/testing

COPY *.el /opt/

RUN emacs --batch --load /opt/army-config.el

ENTRYPOINT ["emacs", "-Q", "--script"]

CMD ["/opt/publish.el"]
