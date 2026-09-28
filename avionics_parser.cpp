#include <iostream>
#include <string>

// Flight Computer Avionics Packet Parser in C++
struct TelemetryPacket {
    float altitude;
    float verticalVelocity;
    float pitch;
    float roll;
    bool parachuteArmed;
};

void parseSensorStream(const TelemetryPacket& packet) {
    std::cout << "[AVIONICS C++ CORE] Processing Sensor Frame:" << std::endl;
    std::cout << "  -> Altitude: " << packet.altitude << " m" << std::endl;
    std::cout << "  -> Attitude (P/R): " << packet.pitch << " deg / " << packet.roll << " deg" << std::endl;
    
    if (packet.altitude > 100.0f && packet.verticalVelocity <= 0.0f) {
        std::cout << "  -> CRITICAL: Apogee Detected! Sending Ejection Command to Pyro Channel 1." << std::endl;
    }
}

int main() {
    TelemetryPacket currentFrame = {450.5f, -0.2f, 88.4f, 2.1f, true};
    parseSensorStream(currentFrame);
    return 0;
}