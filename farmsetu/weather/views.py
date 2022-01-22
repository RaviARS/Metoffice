import requests
import csv, time

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from .models import Weather
from .serializers import WeatherSerializer, ClimateSerializer


class ClimateAPI(APIView):
    """ Get Climate data from met office. """

    serializer_class = ClimateSerializer

    def post(self, request):
        """ Create the Climate CSV. """
        try:
            serializer = ClimateSerializer(data=request.data, context={'request': request})
            if not serializer.is_valid(raise_exception=True):
                raise Exception("Error: Invalid request payload data.")
            request_payload = serializer.data
            print("request_payload", request_payload)

            order_by_keys = ("ranked", "date")
            region_keys = (
            "UK", "England", "Wales", "Scotland", "Northern_Ireland", "England_and_Wales", "England_N", "England_S",
            "Scotland_N", "Scotland_E", "Scotland_W", "England_E_and_NE", "England_NW_and_N_Wales", "Midlands",
            "East_Anglia", "England_SW_and_S_Wales", "England_SE_and_Central_S")
            parameter_keys = ("Tmax", "Tmin", "Tmean", "Sunshine", "Rainfall", "Raindays1mm", "AirFrost")

            order_by = request_payload.get("order_by", "date")
            region = request_payload.get("region", "UK")
            parameter = request_payload.get("parameter", "Tmax")
            req_method = "GET"

            # Request payload data Validation
            if not (order_by in order_by_keys or region in region_keys or parameter in parameter_keys ) :
                raise "Error"

            end_point = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter}/{order_by}" \
                        f"/{region}.txt"
            print("end_point", end_point)
            response_data = requests.request(req_method, end_point)
            print(response_data)
            result = response_data.content.decode("utf-8")
            climate_list = result.split("\n")
            print(climate_list)

            # csv header names
            header_names = climate_list[5].split("   ")
            print(header_names)

            #  Write climate data into csv file
            csv_file_path = f'weather_report/{order_by}/{region}_{parameter}_climate.csv'
            with open(csv_file_path, 'w', encoding='UTF8', newline='') as climate_file:
                write = csv.writer(climate_file)
                write.writerows([climate.split("   ") for climate in climate_list[5:-1]])

            # time.sleep(5)
            # csv_file_path = "/home/ars/Documents/ARS/github/Metoffice/farmsetu/weather_report/"
            with open(csv_file_path, ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:

                    weather_obj = Weather(year=row['year'], jan=row[' jan'], feb=row[' feb'], mar=row[' mar'],
                                          apr=row[' apr'], may=row[' may'], jun=row[' jun'], jul=row[' jul'],
                                          aug=row[' aug'], sep=row[' sep'], oct=row[' oct'], nov=row[' nov'],
                                          dec=row[' dec'], win=row['  win'], spr=row['  spr'], sum=row['  sum'],
                                          aut=row['  aut'], ann=row['  ann'], region=region)
                    weather_obj.save()

            msg = "successfully Added the  MetOffice weather data into the database."
            return Response({"response": msg}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Bad request. Error {e}", status=status.HTTP_400_BAD_REQUEST)


class WeatherListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all().order_by('id')

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class WeatherDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()
    lookup_field = 'id'

    def get(self, request, id=id):
        return self.retrieve(request, id)

    def put(self, request, id=id):
        return self.update(request, id)

    def delete(self, request, id=id):
        return self.destroy(request, id)
