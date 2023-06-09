import React, { useState, useEffect } from 'react';
import { Gyroscope } from 'expo-sensors';
import { StyleSheet, Text, View } from 'react-native';
import axios from 'axios';

const URL_TRAIN = 'http://10.50.34.198:8000/gyro_train_';
const URL_LIVE = 'http://10.50.34.198:8000/live';

export default function GyroData(props) {
  const [data, setData] = useState({ x: 0, y: 0, z: 0 });
  const [send, setSend] = useState(props.isOn ? true : false);
  const [record, setRecord] = useState(props.record ? true : false);
  const [movement, setMovement] = useState(props.movement);
  const [endpoint, setEndpoint] = useState(props.isEnabled ? URL_LIVE : URL_TRAIN+movement);

  const [acclData, setAcclData] = useState(props.acclData);

  useEffect(() => {
    setAcclData(props.acclData);
  }, [props.acclData]);

  useEffect(() => {
    setMovement(props.movement);
  }, [props.movement]);

  useEffect(() => {
    setEndpoint(props.isEnabled ? URL_LIVE : URL_TRAIN+movement);
  }, [props.isEnabled, movement]);

  useEffect(() => {
    setSend(props.isOn ? true : false);
  }, [props.isOn]);

  useEffect(() => {
    setRecord(props.record ? true : false);
  }, [props.record]);

  useEffect(() => {
    let subscription = null;
    let timeout = null;
    let arrData = [];

    async function setupGyro() {
      subscription = await Gyroscope.addListener((gyroData) => {
        setData(gyroData);
        if (record) {
          if (!props.isEnabled){
            arrData.push(gyroData);
            if (timeout === null) {
              timeout = setTimeout(() => {
                console.log(`Endpoint: ${endpoint}\n Gyro-Data: ${JSON.stringify(arrData)}`);
                if (send && !endpoint.includes("undefined")) {
                  axios.post(endpoint, arrData);
                }  
                arrData = [];
                props.toggleRecord();
                clearTimeout(timeout);
                timeout = null;
              }, 10000);
            }
          }
          else {
            if (send) {
              if (acclData != undefined){
                let sensorData = {
                  "gyro":gyroData,
                  "accl": acclData,
                }
                axios.post(endpoint, sensorData);
                console.log(`SensorData: ${JSON.stringify(sensorData)}`);
              }
            }  
          }
        }
      });
    }

    setupGyro();

    return () => {
      if (subscription) {
        subscription.remove();
      }
    };
  }, [endpoint, send, record, movement, acclData]);

  return (
    <View style={styles.container}>
       <Text style={styles.text}>Gyroscope:</Text>
       <Text style={styles.text_data}>x,y,z: {data.x.toFixed(2)},{data.y.toFixed(2)},{data.z.toFixed(2)}</Text>
       <Text style={styles.text_endpoint}>Sending Data to: {endpoint}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center'
  },
  text: {
    fontSize: 18,
    fontWeight: 'bold',
    marginVertical: 5,
    margin: 10
  },
  text_data: {
    fontSize: 18,
    marginVertical: 5,
    margin: 10
  },
  text_endpoint: {
    fontSize: 12,
    marginVertical: 5,
    margin: 10
  },
});
