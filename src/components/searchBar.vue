<template>
  <div class="searchBar" @keyup.enter="handler">
      <input type="text" placeholder="ville" v-model="city" >
      <button @click="handler">

      </button>
  </div>
</template>

<script setup>
import {ref} from "vue"

let city = ref("")
let emit = defineEmits(["data"])
function handler(){
    emit("findCity",city.value)
}
</script>
<style>

button{
    background: url("../assets/search.svg") center center no-repeat;
    padding: 10px;
}
.searchBar{
    width: 50%;
    margin:100px ;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    border-radius: 5px;
    padding: 5px;
    display: flex;
    align-items: center;
}
.searchBar *{
    vertical-align: middle;
    height: 100%;
    border:none;
    outline: none; 
    padding: 9px;
}
.searchBar input{
    width: 85%;
}
.searchBar button{
    width: 15%;
    vertical-align: middle;
}
@media screen and (max-width:680px){
    .searchBar{
        width: 70%;
    }
}
.searchBar input::placeholder{
    text-align: center;
}
</style>
