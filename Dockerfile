# Copyright 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:10
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    vim \
    nano \
    tree \
    htop \
    wget \
    curl \
    unzip \
    ca-certificates \
    openssl \
    python \
    python-dev \
    libyaml-dev

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
RUN python2 get-pip.py
RUN python2 -m pip install --upgrade setuptools
RUN python2 -m pip install --upgrade pip
RUN python2 -m pip install --upgrade build
RUN rm -f get-pip.py
COPY requirements.txt /
RUN pip2 install -r requirements.txt
RUN rm -f requirements.txt
RUN mkdir /manage_commands/
COPY manage_commands /manage_commands/
COPY manage.py /
RUN find /manage_commands/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN mkdir /app_server/
COPY app_server /app_server/
RUN find /app_server/ -name "*.editorconfig" -type f -exec rm -Rf {} \;
RUN mkdir /FlaskApp/
RUN mv manage.py /FlaskApp/
RUN mv /manage_commands/ /FlaskApp/
RUN mv /app_server/ /FlaskApp/
RUN rm -rf /manage_commands/
RUN rm -rf /app_server/
RUN chmod -R 755 /FlaskApp/
RUN tree /FlaskApp/
