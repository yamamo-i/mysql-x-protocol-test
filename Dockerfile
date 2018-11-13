FROM mysql:8.0.13

RUN set -x \
    && apt update \
    && apt install -y wget net-tools libpython2.7 \
    && apt --fix-broken install \
    && (cd tmp && wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell_8.0.13-1debian9_amd64.deb && dpkg -i mysql-shell_8.0.13-1debian9_amd64.deb) \
    && (cd tmp && wget https://dev.mysql.com/get/Downloads/MySQL-Shell/mysql-shell-dbgsym_8.0.13-1debian9_amd64.deb && dpkg -i mysql-shell-dbgsym_8.0.13-1debian9_amd64.deb) \
    && rm /tmp/*.deb \
    && netstat -tan

