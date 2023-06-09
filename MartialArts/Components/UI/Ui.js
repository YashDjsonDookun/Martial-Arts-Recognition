import React, { useState, useEffect, useRef, useCallback, onChange } from 'react';
import { Button, StyleSheet, Switch, Text, View } from 'react-native';
import SensorData from './SensorData/Sensors/SensorData';
import DropDownPicker from "react-native-dropdown-picker";

export default function Ui() {
  const [isEnabled, setIsEnabled] = useState(false);
  const [isOn, setIsOn] = useState(false);
  const [record, setRecord] = useState(false);
  const [movement, setMovement] = useState(gender);
  const [genderOpen, setGenderOpen] = useState(false);
  const [genderValue, setGenderValue] = useState(null);
  const [gender, setGender] = useState([
    { label: "Jodan-Ooke (Upper Block)", value: "jodan_ooke" },
    { label: "Choodan-Ooke (Middle Block)", value: "choodan_ooke" },
    { label: "Gedan-Ooke (Lower Block)", value: "gedan_ooke" },
    { label: "Jodan-Zooki (Upper Punch)", value: "jodan_zooki" },
    { label: "Choodan-Zooki (Middle Punch)", value: "choodan_zooki" },
    { label: "Gedan-Zooki (Lower Punch)", value: "gedan_zooki" },
    { label: "Random", value: "random" },
  ]);

  const handleChoice = () => {
    setMovement(genderValue);
  };
  
  const toggleRecord = ()=> {
    setRecord(previousState => !previousState);
  };

  // useEffect(()=> {
  //   // console.log(movement);
  // }, [movement])

  return (
    <View style={styles.container}>
          <View style={styles.dropdownGender}>
            <DropDownPicker
              style={styles.dropdown}
              open={genderOpen}
              value={genderValue} //genderValue
              items={gender}
              setOpen={setGenderOpen}
              setValue={setGenderValue}
              setItems={setGender}
              placeholder="Select Movement"
              placeholderStyle={styles.placeholderStyles}
              onChangeValue={handleChoice}
              zIndex={1}
              zIndexInverse={1}
            />
        </View>
        {movement == undefined && !isEnabled ? <Text style={{margin: 20, color: "red", textAlign: "center"}}>WARNING: No Movement Selected - Data will be disregarded for training!</Text> : ""}
        <SensorData isEnabled={isEnabled} isOn={isOn} record={record} toggleRecord={toggleRecord} movement={movement}/>
        <View style={styles.switchContainer}>
          <Text style={{marginRight: 10}}>Data Collection</Text>
          <Switch
              trackColor={{false: '#767577', true: '#81b0ff'}}
              thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
              ios_backgroundColor="#3e3e3e"
              onValueChange={value => setIsEnabled(value)}
              value={isEnabled}
          />
          <Text style={{marginLeft: 10}}>Live Testing</Text>
        </View>
        {isEnabled ? <Text style={styles.text}>Live Demo: ON</Text> : ""}
        <View style={styles.switchContainer}>
          <Text style={{marginRight: 10}}>ALLOW SENDING - OFF</Text>
          <Switch
              trackColor={{false: '#767577', true: '#81b0ff'}}
              thumbColor={isOn ? '#f5dd4b' : '#f4f3f4'}
              ios_backgroundColor="#3e3e3e"
              onValueChange={value => setIsOn(value)}
              value={isOn}
          />
          <Text style={{marginLeft: 10}}>ALLOW SENDING - ON</Text>
        </View>
        <View style={styles.switchContainer}>
          <Text style={{marginRight: 10}}>RECORD OFF</Text>
          <Switch
              trackColor={{false: '#767577', true: '#81b0ff'}}
              thumbColor={record ? '#f5dd4b' : '#f4f3f4'}
              ios_backgroundColor="#3e3e3e"
              onValueChange={toggleRecord}
              value={record}
          />
          <Text style={{marginLeft: 10}}>RECORD ON</Text>
        </View>
    </View>
  );
}
const styles = StyleSheet.create({
  switchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingBottom: 25
  },
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  dropdownGender: {
    marginHorizontal: 10,
    width: "50%",
    marginBottom: 220,
  },
});