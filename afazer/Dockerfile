FROM python
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN mkdir /service
COPY afazer/ /service/afazer/
COPY protobuf/ /service/protobuf/
COPY Usuario/ /service/Usuario/
WORKDIR /service/afazer
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
WORKDIR ../usuario
RUN python -m grpc_tools.protoc -I ../protobuf --python_out=. --grpc_python_out=. ../protobuf/usuarios.proto
WORKDIR ../afazer
EXPOSE 50051
ENV FLASK_APP=afazer.py

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]