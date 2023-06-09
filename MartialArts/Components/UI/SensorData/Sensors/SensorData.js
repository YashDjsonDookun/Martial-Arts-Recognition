import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Acc_data from './Acc_data';
import Gyro_Data from './Gyro_Data';

export default function SensorData(props) {
  const [acclData, setAcclData] = useState();

  return (
    <View style={styles.container}>
        <Text>
          <Acc_data isEnabled={props.isEnabled} isOn={props.isOn} record={props.record} toggleRecord={props.toggleRecord} movement={props.movement} setAcclData={setAcclData}/>
        </Text>
        <Text>
          <Gyro_Data isEnabled={props.isEnabled} isOn={props.isOn} record={props.record} toggleRecord={props.toggleRecord} movement={props.movement} acclData={acclData}/>
        </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff'
  },
});
