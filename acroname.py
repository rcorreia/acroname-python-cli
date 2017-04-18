#!/usr/bin/env python
import optparse
import brainstem

def main():
  p = optparse.OptionParser()
  p.add_option('--port', type='int', dest='port', help='USB port number')
  p.add_option('--enable', action='store_true', dest='enable', help='Enable USB port')
  p.add_option('--disable', action='store_true', dest='disable', help='Disable USB port')
  p.add_option('--cycle', action='store_true', dest='cycle', help='Disables then Enables USB port')

  options, arguments = p.parse_args()

  stem = brainstem.stem.USBHub3p()
  stem.discoverAndConnect(brainstem.link.Spec.USB)

  if options.enable == True:
      print 'Enabling Hub Port: %s' % options.port
      stem.usb.setPortEnable(options.port)
  elif options.disable == True:
      print 'Disable Hub Port: %s' % options.port
      stem.usb.setPortDisable(options.port)
  elif options.cycle == True:
      print 'Cycling Hub Port: %s' % options.port
      stem.usb.setPortDisable(options.port)
      from time import sleep
      sleep(2)
      stem.usb.setPortEnable(options.port)
  else:
    print 'You must specify a port state with the --enable, --disable, or --cycle option'

  stem.disconnect()

if __name__ == '__main__':
  main()
