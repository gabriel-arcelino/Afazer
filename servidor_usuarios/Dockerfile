FROM python
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /service

COPY Admin/ /service/Admin/
#WORKDIR /service
#RUN mkdir /protobuf
COPY protobuf/ /service/protobuf/
COPY Usuario/ /service/Usuario/
WORKDIR /service/Admin
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt
#RUN mkdir /Usuario
WORKDIR ../usuario
RUN python -m grpc_tools.protoc -I ../protobuf --python_out=. --grpc_python_out=. ../protobuf/usuarios.proto
CMD ["sed -i '1c import sys, os sys.path.append(os.path.dirname(os.path.abspath(__file__)))' usuarios_pb2.py"]
WORKDIR ..
EXPOSE 50051
#ENV FLASK_APP=app.py

#ENTRYPOINT [ "flask", "run"]
ENTRYPOINT [ "python", "-m"]
CMD ["Admin.app"]