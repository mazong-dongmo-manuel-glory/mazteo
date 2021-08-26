<template>
  <searchBar @findCity="findCity"></searchBar>
  <boxView></boxView>
  <footer>
    <a href="https://ozoowi.herokuapp.com">mazong</a> Copyright &copy; 2021
  </footer>
</template>

<script setup>
import searchBar from "./components/searchBar.vue"
import boxView from "./components/boxView.vue" 
import {provide, ref} from "vue"
let content = ref({}) 
let state = ref(null)
provide("content",content) 
provide("state",state)
function findCity(city){
    let xhr = new XMLHttpRequest()
    if(city != ""){
        xhr.open("GET","https://api.weatherapi.com/v1/current.json?key=81caf41e3d924f5086a150502211108&q="+city)
        xhr.onreadystatechange = function(ev){ 
            if(xhr.readyState == 4){
                if(JSON.parse(xhr.responseText).error){
                  content.value = undefined
                  state.value = false

                }else{

                
                content.value = JSON.parse(xhr.responseText)
                state.value = false
                }
            }
        }
        state.value = true  

        xhr.send()
        city = ""
    }
}
</script>

<style>
*{
  box-sizing: border-box;
  text-decoration: none;
}
body{
  margin: 0;
  padding: 0;
  position: relative;
  overflow: hidden;
}
#app {
  font-family: montserrat;
  min-height: 100vh;
  width: 100%;
  position: relative;
  display: flex;
 align-items: center;
 flex-direction: column;
}
footer{
  position: absolute;
  bottom: 0;
  padding: 10px;
}
footer a{
  color: rgb(0, 89, 255);
}
</style>
