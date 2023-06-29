import dpkt
import socket
import pygeoip

## dpkt is a module for working with packet capture (pcap) files.
##socket provides functions to convert IP addresses from binary to text format.
##pygeoip is a library for geolocating IP addresses using a GeoIP database.

gi = pygeoip.GeoIP('GeoLiteCity.dat')


def retKML(dstip, srcip):
    dst = gi.record_by_name(dstip)
    src = gi.record_by_name('x.xxx.xxx.xxx')  ##Internal ip for traffic check
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        return ''
## The retKML function takes a destination IP address (dstip) and source IP address (srcip) as input and returns a KML (Keyhole Markup Language) string. KML is a format used to display geographic data in applications like Google Earth.

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = retKML(dst, src)
            kmlPts = kmlPts + KML
        except:
            pass
    return kmlPts
##The plotIPs function takes a pcap file (pcap) as input and iterates over the packets in the file.
##For each packet, it extracts the source and destination IP addresses.
##It calls the retKML function to generate a KML string based on the IP addresses.
##The generated KML strings are concatenated and returned.


def main():
    f = open('wire.pcap', 'rb')
    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n' \
                '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
    print(kmldoc)


if __name__ == '__main__':
    main()
##The main function is the entry point of the program.

##It opens the wire.pcap file in binary mode using dpkt.pcap.Reader.
#It defines the KML header, which includes the XML declaration and the KML namespace.
#It defines the KML footer.
#It calls the plotIPs function to generate the KML placemarks based on the packets in the pcap file.
#The KML header, generated KML placemarks, and KML footer are concatenated to form the complete KML document.
#The resulting KML document is printed to the console.
#The if __name__ == '__main__': block ensures that the main function is only executed when the script is run directly, not when it is imported as a module.