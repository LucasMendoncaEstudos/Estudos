import React,{Component} from 'react';
import { View, Text , StyleSheet, TextInput, Image, TouchableOpacity} from 'react-native';

class App extends Component{
  constructor(props){
    super(props)
    this.state ={
      textoFrase: '',
      img:require('./src/biscoito.png')
    }
    this.quebraBiscoito = this.quebraBiscoito.bind(this)
    this.frases = [
      'Teste1',
      'Teste2',
      'Teste3',
      'Teste4'
    ]
  }
  quebraBiscoito(){
    let numeroAleatorio = Math.floor(Math.random() * this.frases.length)
    this.setState({
      textoFrase: '"'+this.frases[numeroAleatorio] + '"',
      img: require('./src/biscoitoAberto.png')
    })

  }
  render(){
    return(
      <View style = {styles.container}>

        <Image source={require('./src/biscoito.png')}
        style={styles.img}/>

        <Text style={styles.textoFrase}>" Alguma frase aqui "</Text>

        <TouchableOpacity style={styles.botao} onPress={this.quebraBiscoito}>
          <View style={styles.btnArea}>
            <Text style={styles.btnTexto}>Quebrar Biscoito</Text>
          </View>
        </TouchableOpacity>
      </View>
      
    )
  }
}
const styles = StyleSheet.create({
  container:{
    flex:1,
    alignItems:'center',
    justifyContent:'center'
  },
  img:{
    width:250,
    height:250
  },
  textoFrase:{
    fontSize:20,
    color:'#dd7b22',
    margin:20,
    fontStyle:'italic',
    textAlign:'center'
  },
  botao:{
    width:230,
    height:50,
    borderWidth:2,
    borderColor:'#dd7b22',
    borderRadius:25
  },
  btnArea:{
    flex:1,
    flexDirection:'row',
    justifyContent:'center',
    alignItems:'center'
  },
  btnTexto:{
    fontSize:28,
    fontWeight: 'bold',
    color:'#dd7b22'
 }
})
export default App;