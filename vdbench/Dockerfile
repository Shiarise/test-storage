FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        csh \
        default-jre \
    && apt-get clean \

ENV PATH /usr/local/bin:$PATH

RUN apt-get install -y \
    python \
    python3-pip

RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install PyYAML
RUN pip3 install matplotlib
RUN pip3 install pyyaml

COPY vdbench vdbench.jar bench_runner.sh runVdbench.py /
COPY templates /templates/

CMD ["python", "runVdbench.py","templates/inputYAML/Basic/File_Basic_Read_Write.yml"]

#CMD ["ls"]
