FROM ubuntu:latest
RUN apt-get update -qqy && apt-get install -qqy curl make \
 && rm -rf /var/apt/cache 
RUN curl -o /vector.tar.gz https://packages.timber.io/vector/0.15.0/vector-0.15.0-aarch64-unknown-linux-gnu.tar.gz \
 && mkdir -vp /vector \
 && tar -xzC /vector -f /vector.tar.gz \
 && mv /vector/vector-aarch64-*/* /vector/ \
 && rm -rvf /vector.tar.gz vector-aarch64-*
WORKDIR /vector
COPY ./vector.d /vector/config.d
ENV VECTOR_CONFIG_TOML="/vector/config.d/*.toml"
ENTRYPOINT [ "/vector/bin/vector"]
