FROM centos:7

ENV LANG C.UTF-8
ARG url=https://github.com/tuimac/tagdns.git

WORKDIR /root

ADD env/vimrc /root/.vimrc
ADD env/bashrc /root/.bashrc
ADD env/login_screen /root/.login_screen
ADD env/centos/vim.sh /etc/profile.d/vim.sh
ADD env/tmux.conf /root/.tmux.conf

ADD requirements.txt /root/requirements.txt

RUN yum update -y && \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \
    yum remove -y vi && \
    yum install -y python36u python36u-libs python36u-devel python36u-pip \
                    vim* iproute curl iputils-ping net-tools git bind-utils && \
    git clone $url && \
    mkdir -p ~/.vim/backup && \
    mkdir -p ~/.vim/undo && \
    mkdir -p ~/.vim/swap
