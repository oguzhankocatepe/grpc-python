import time
import grpc
from concurrent import futures
from plane_pb2 import Plane, Planes
from plane_pb2_grpc import PlaneServiceServicer, add_PlaneServiceServicer_to_server

class PlaneService(PlaneServiceServicer) :
    planes = [Plane(name = "Plane1", x= 10,y = 10,z = 10)]
    id = 0
    def CreatePlane(self, request, context):
        self.id += 1
        plane = Plane(id = self.id ,name = request.name, x= request.x, y = request.y,z = request.z)
        self.planes.append(plane)
        return plane
    def GetPlanes(self, request, context):
        return Planes(planes=self.planes)
    def StreamPlanes(self, request, context):
        for i in range(10):
            yield Planes(planes=self.planes)
            time.sleep(1)
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PlaneServiceServicer_to_server(PlaneService(),server)
    server.add_insecure_port("[::]:" +  port)
    server.start()
    print ("Server started on port" + port)
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

    #with grpc.insecure_channel('localhost:50051') as channel:
    #    stub = PlaneServiceStub(channel)
    #    response = stub.CreatePlane(PlaneNoId("plane1",10,10,10));
    #    print (response.message)
    #    response = stub.GetPlanes(GetPlanesRequest());
    #    print (response.message)        