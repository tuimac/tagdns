FROM alpine:latest

WORKDIR /root

EXPOSE 53

ADD requirements.txt /root/requirements.txt
ADD entrypoint.sh /root/entrypoint.sh

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash git icu-dev ncurses icu-libs vim python3 python3-dev py3-pip curl tree && \
    mkdir /etc/vim/backup && \
    mkdir /etc/vim/undo && \
    pip3 install -r requirements.txt && \
 	rm /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/vim/vimrc -o /etc/vim/vimrc && \
    curl -L https://raw.githubusercontent.com/tuimac/tools/master/linux/bashrc/.bashrc_node_docker -o /root/.bashrc && \
    git clone https://github.com/tuimac/tagdns && \
    git config --global user.email "tuimac.devadm01@gmail.com" && \
    git config --global user.name "tuimac"

ENTRYPOINT ["/root/entrypoint.sh"]
