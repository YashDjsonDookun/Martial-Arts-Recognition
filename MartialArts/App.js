// import React, { useState, useEffect } from 'react';
import { StyleSheet, View } from 'react-native';
import Ui from './Components/UI/Ui';

export default function App() {
  return (
    <View style={styles.container}>
      <Ui/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});