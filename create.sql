-- Drop existing tables if they exist
DROP TABLE IF EXISTS overall_satisfaction CASCADE;
DROP TABLE IF EXISTS satisfaction_ratings CASCADE;
DROP TABLE IF EXISTS delays CASCADE;
DROP TABLE IF EXISTS flights CASCADE;
DROP TABLE IF EXISTS passengers CASCADE;

-- Create Passengers Table
CREATE TABLE passengers (
    PassengerID SERIAL PRIMARY KEY,  -- Auto-incremented ID for passengers
    Gender VARCHAR(10) NOT NULL DEFAULT 'Not Specified',
    CustomerType VARCHAR(50) DEFAULT 'Disloyal Customer',
    Age INTEGER NOT NULL CHECK (Age >= 0)
);

-- Create Flights Table
CREATE TABLE flights (
    FlightID INTEGER PRIMARY KEY,  -- Unique flight identifier (created manually)
    FlightDistance FLOAT NOT NULL DEFAULT 0.0,
    TypeOfTravel VARCHAR(50) NOT NULL DEFAULT 'Personal Travel',
    Class VARCHAR(20) NOT NULL DEFAULT 'Economy'
);

-- Create Satisfaction Ratings Table
CREATE TABLE satisfaction_ratings (
    RatingID SERIAL PRIMARY KEY,  -- Auto-incremented ID for each rating
    PassengerID INTEGER NOT NULL REFERENCES passengers(PassengerID) ON DELETE CASCADE,
    FlightID INTEGER NOT NULL REFERENCES flights(FlightID) ON DELETE CASCADE,
    InflightWifiService INTEGER NOT NULL CHECK (InflightWifiService BETWEEN 0 AND 5),
    SeatComfort INTEGER NOT NULL CHECK (SeatComfort BETWEEN 0 AND 5),
    EaseOfOnlineBooking INTEGER NOT NULL CHECK (EaseOfOnlineBooking BETWEEN 0 AND 5),
    FoodAndDrink INTEGER NOT NULL CHECK (FoodAndDrink BETWEEN 0 AND 5),
    InflightEntertainment INTEGER NOT NULL CHECK (InflightEntertainment BETWEEN 0 AND 5),
    OnboardService INTEGER NOT NULL CHECK (OnboardService BETWEEN 0 AND 5),
    GateLocation INTEGER NOT NULL CHECK (GateLocation BETWEEN 0 AND 5),
    LegRoomService INTEGER NOT NULL CHECK (LegRoomService BETWEEN 0 AND 5),
    Cleanliness INTEGER NOT NULL CHECK (Cleanliness BETWEEN 0 AND 5)
);

-- Create Delays Table
CREATE TABLE delays (
    DelayID SERIAL PRIMARY KEY,  -- Auto-incremented ID for each delay record
    FlightID INTEGER NOT NULL REFERENCES flights(FlightID) ON DELETE CASCADE,
    DepartureDelayInMinutes FLOAT DEFAULT 0,
    ArrivalDelayInMinutes FLOAT DEFAULT 0
);

-- Create Overall Satisfaction Table
CREATE TABLE overall_satisfaction (
    SatisfactionID SERIAL PRIMARY KEY,  -- Auto-incremented ID for each satisfaction record
    PassengerID INTEGER NOT NULL REFERENCES passengers(PassengerID) ON DELETE CASCADE,
    Satisfaction VARCHAR(40) NOT NULL DEFAULT 'Neutral'
);
