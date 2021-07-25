FROM docker-dev.artifactory.company.com/centos:7.3.1611

***************************************
Existing commands in the Dockerfile
***************************************

RUN yum install -y krb5-devel
RUN yum install -y python-devel
RUN yum install -y krb5-workstation
RUN yum install -y python-setuptools
RUN yum install -y python-pip

FROM ubuntu:16.04
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        csh \
        default-jre \
    && apt-get clean


COPY vdbench vdbench.jar bench_runner.sh /
COPY linux /linux/
COPY templates /templates/

CMD ["/bench_runner.sh"]
