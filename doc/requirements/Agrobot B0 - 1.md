# Agrobot B0 - Requirements

```
Author: Nicholas Mc Guire
Review: 0.2
Date: May 7, 2019
Expires: Nov 8, 2019
Keywords: B0 requirements, basic data aquisition only.
Status: initial draft, unreviewed
DLC Phase: requiremnts
Ref: TODO add HW manuals
QA: initial review
Tracking: GIT
Format: ascii text
```

## Outline:

Basic collection of requirements based primarily on discussions and
team-meetings as well as some preliminary experimentation to gain rough
limits. These requirements serve as the basis for the design,
implementation and initial operation phase of B0.

## Intent of B0:

  Provide minimal mechanical and electrical/electronical support for
  data quisition on a fixed (track-bsaed) potatoe-"field" while
  assuring basic (minimal) safety properties.

## Software controler (Arduino)

 ### Arduino statup 
   - Provide ready signal once booted ? e.g. Pi can 
     request status -> response ready-for-command, busy-calibrate or
     error-state (to be defined !)
 ### Control of 4 drive-motors 
   - Input (from Pi3) relative motion distance/direction e.g.
     (+10cm/-20cm) 
   - Reset information (at end of track) to Pi ?? open-issue
   - Accuracy over the entire track (12m) +/- 3m (duable ?)
 ### Control of y-axis sled motor
   - Input (from Pi3) relative motion command (e.g. +5cm/-10cm)
   - Response Ack (e.g. 0 ok, -1 failed to execute command or
     error code about the failure 1 reset ?? TBD)
   - Reset information to Pi ?? open-issue
   - Accuracy over the entire sled (1m) +/- 2m (duable ?)
 ### Continuous check of end-pos sensors
   - (TOF Ultrasound for X-axis)
   - Read-contacts for y-axis (in discussion)
   - End bumpers on y-axis (ruber aprox 2cm)
   - End wheel catchers for X-axis in dicussion)
 ### Motion requirements
   - X-axis maximum speed 50-80 cm/min
   - Y-axis maximum 30cm/min (roughly 3 minutes for a left-right pass)
   - Reset of absolute 0 every 5m (2.5 passes ? or make that 6m and 
     3 full passes ?)
 ### Power Management requirements 
   - 5V supply for
        - Arduino
        - Raspberry Pi3
        - servo-motors 
        - LEDs
   - 30V for motors (?)
   
    Power supplies need to be sufficiently independent with respect
    to disturbances (notably the 30V!) TBD specify tollerances
    Voltage regulators for 5V and 30V shall be provided on-board
    based on 220V/60Hz source (atleast thats what I think china
    uses ?)
 

## Mechanical motion requirements

 The track (X-axis) is covered from end-to-end
   - Total travel time roughly 1h
 The sled (Y-axis) is covered from end-to-end
   - a pre-specified (static) number of halting positions is defined
   - continuous motion in discussion
 2 Cameras can be mounted on the Y-axis (USB connected to Pi3) 
 Side-guards on all 4 wheels
   - possitional accuracy on the track +/- 2cm
 Cable caryiage - power and network
 End-plates for reliable ultrasound reflection
   - Material (Al probably ?) TBD
   - Diameter 15cm ? TBD 
 Motors outward oriented - no collision with plants
   - Wheels "point" inward 

## Structural mechanics requirements (bot)

 headway/headroom: (over track) 80-90cm (all structural elements - not 
   counting sensor/actor fixtures)
 clear width: 100cm (ideally the wheels are the inner most point - which
   may be a bit below 100cm (95-96cm clear width between wheels)
 structural length <= 90cm total (including wheels !)
 top-torsion structure
   - couble-frame cage (possibly with surface re-inforcement pannels)
   - hights 10-15cm
   - single (uninterrupted) beams on each side
   - corner re-inforcmenets "on demand" TBD
 Whele legs - bending limits/deflection under assumed maximum force (TBD !)
   - sidewards (Y-direction deflectino <= 1cm ?? can we put a lower bound
     on this ?
   - longitudinal (X-direction) deflection <= 0.5cm - if needed insert an
     additional stiffening element between the legs.

## Structural requirements bed

 Soil container dimensions 12x1*0.45m (initially 0.5 but reduced due to
   material availability)
 Double water protection in-side (silicon paint + plastic cover)
 Load distribution to cover 18 m^2 (<= 300kg/m^2 - which is for sure
   below load limits of the roof)
 Side props to support soil pressure (depends on board dimensions and
   quality)
 Tracks on both length side 
   - Min width 7-8cm
   - Surface plane +/- 1cm over the lenthg (should be achievable)
   - One-sided tape-mount for position recording (X-axis)
 Power rail (suspension) for draging of power/network cable
   (drag chain cable carrier or 
 Cabling requirements 
   - Electric cabling provided (220V)
   - Network (100Mbit ?) provided
   - other TBD

## Safety requirements

 The robot frame structure must be grounded !
 The cable caryiage must be grounded !
 The network cable shall be reasonably potential free (Tollerance TBD)
 All power cables shall be protected by adequate cable strain reliefs

Structural mechanics requirements (bot)
 USB cables shall be supported by a kinematic support (or similar)
   to ensure that sled movement can not damage/squeeze the 
   cabling
 Servo cables ? length limit ? TBD - not clear if the servos
   can be connected over 1.2m cable legth (voltage drop ?)
 Ultra-sound receiver cables - length limit ? TBD
 I2C <-> PWN-controller cable - mechanical stability TBD

## Application sensor/actor requirements

 Low resolution camera capturing track position (tape) 
 
 ### Condition monitoring
   - Humidity sensor - Accuracy ??
   - Temperatur sensor - Accuracy ??
   - Air pressure sensor - Accuracy ??
   - Sample rate 4-6 times per day (TBD)
 ### High-resolution camera for still pictures
   - 1280/720 minimum 
   - 24 bit collor resolution
 ### High-resolution camera for video
   - FPS ??
   - resolution ??
   - Format ??
 ### LED lines
   - R/G/B other ?
   - brightness control (e.g. PWM)
 ### 2-axis servo for camera gimbal
 Structural mechanics requirements sensor mounting
   - Still image camera Y-axis sled mounted with  U/V rotation (180)
   - Video camera Y-axis firm streight-down mount
   - stationary low-res Video camera mount-point on leg 10-15 cm 
     above track (test focus range needed)

## Imaging requirements

 Still-image rate ?
 Video format 
 Storage format

## Application processor requirements (Pi3)

 ### Communication/synchronisation Arduino
   - Communication via serial line - clear-text - no security requirements
     o data CRC ?
   - Command send and status receive
     o loging of command sequence
   - Camera imaging commands (synchronized with arduino potition control)
   - Camera gimbaling control and angular recording (probably in image name
     TBD)
 ### Communication requirements Server
   - 100 Mbit or Gbit connection 
   - SSH server 
     o remote login support for non-root user
     o pre-exchanged keys 
     o DSA keys
   - rsync support: rsync over ssh for data retrival (pull from server)
   - defined security policy (TBD)
 ### Sensor handling
   - manage all sensors (implemented in python)
     o I2C bus configuration and handling
     o USB configuration and handling
   - manage LEDs (collor/intensity and sync with imaging subsystem)
 ### Data aquisition and handling
   - dedicated storage media for sensor data (not on root fs)
   - high-resolution and low-resolution camera + still-image camera
   - storage of a full track run locally (estimation:
     o still image <=5 images per y-axis transit, <=50 positions along
       the track - image size (jpeg) <= 500k -- 125MB per full track
       transit.
     o high-resolution vide 30GB per full track transit ??
   - Environment data sensor recording
 ### System monitoring
   - Standard Linux system records (syslog/klog/last)  

## Server requirements

Management data requirements
 ### Weathre records for Lanzhou (genreal - public available records)
   - preferably with a local stored daily weather record
 ### Watering records
   - Ammount (number of watering cans - roughly euqally filled)
   - Time (+/-30min)
   - Person
 ### Operations records
   - Number of traversals and time and any anomalies
   - Number of photos/video-length per traversal and any anomalies
   - Number of environment sensor records and any anomalies
   - Motion record
     o Motion accuracy at end of track (X-axis)
     o Motion accuracy at reset of sled (Y-axis) roughly how many steps
       needed to reach end-indicator
     o Any abnormal termination of motion    
   - Server record
     o Recording of any operational anomalies related to
       data loss or authentication violation