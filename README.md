# mqtt_OPNsense_cpu_temperature

Takes the temperature of the CPU in an OPNsense router and sends it to an MQTT server,

Because it is based on FreeBSD should also be working for PfSense 😀

It checks only the temperature of core zero, you can tune how many cores it checks and whether it averages them or gets the maximum. Honestly I have seen that setting it only for one core is enough cuz they are usually utilized equally.


Run ./pip_dependences.sh to install the python3 dependences
