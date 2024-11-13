from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import configparser


# Crear la clase base de la tabla
class Base(DeclarativeBase):
    pass


# Datos de configuración
config = configparser.ConfigParser()
config.read("proyecto.cfg")
db = config["db"]["db"]
if db == "sqlite":
    system = config["db"]["sqlite"]
elif db == "postgresql":
    system = config["db"]["postgresql"]


# Definir los modelos
class TestData(Base):
    __tablename__ = "test_data"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    timestamp = Column(DateTime)
    data = Column(Integer)
    sunlight = Column(Boolean)
    #Aquí iba la variable_3 pero esta fue borrada ya que el API no contempla esta variable
    
# Crear la conexión a la base de datos SQLite3 o PostgreSQL
engine = create_engine(system)
Session = sessionmaker(bind=engine)
session = Session()

# Crear la(s) tabla(s) en la base de datos
Base.metadata.create_all(engine)
