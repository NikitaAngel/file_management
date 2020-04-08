<template>
    <div class="filemanagement">
        <div class="container1">
            <div class="navigation_bar">
                <p>Learning Analytics</p>
            </div>
            <div class="navigation_bar">
                <nav id="fm_topmenu" class="hidden-xs hidden-sm">
                     <ul class="container1">
                        <li v-for="(item,index) in headNav" :key="index"  @click="handleAClick(item.title)">
                            <router-link :to= "{path: item.url}" :class="[(currentClick === item.title) ? 'aActive' :'aNormal']">
                                {{item.title}}
                            </router-link>
                        </li>
                        <li>
                            <a @click=logOut :class="[(currentClick === 'Log Out') ? 'aActive' :'aNormal']">
                                Log Out
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="fm_container">
            <div class= "container">
                <div class="col-lg-3 col-md-3 col-sm-5 col-xs-10">
                    <div class="file_list">
                        <div class="list_header">
                          <img src="/static/资源 6.png">
                          <img src="/static/资源 5.png">
                          <form>
                          <label>From</label>
                          <input type="date" id="startdate">
                          <label>To</label>
                          <input type="date" id="enddate">
                          <button type="submit">inquire</button>
                          </form>
                          <img src="/static/资源 4.png">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
export default {
  data () {
    return {
      headNav: [
        {title: 'Home', url: '/home'},
        {title: 'Server Monitor', url: '/serve_monitor'},
        {title: 'File Management', url: '/file_management'},
        {title: 'Computation', url: '/computation'},
        {title: 'Data', url: '/data'}
      ],
      currentClick: 'Home'
    }
  }
}
</script>

<style>

  /* div.col-lg-3 {
    display: inline-block;
    margin: 10px;
    padding: 10px;
    border: #DCDCDC solid thin;
    background-color: #fdffff;
    border-radius: 30px;
    text-align: center;
  } */

  div.col-lg-3 p{
    font-size: x-large;
    font-weight: 900;
    color: #000000;
  }

  div.container{
    display: inline-block;
    margin-left: 30px;
    margin-top: 20px;
  }

  div.navigation_bar {
    text-align: center;
    display: inline-block;
    margin-left: 150px;
  }

  div.navigation_bar p{
    font-weight: bolder;
    font-size: 150%;
  }

  ul.container1 li {
    display: inline;
    margin:15px;
    color: #808080;
    font-weight: bold;

  }

  ul.container1 li a {
    text-decoration: none;
    color: #808080;
  }

  div.filemanagement {
    width: 100%;
    height: 100%;
    position: absolute;
    background-color: #FAFAFA;
    overflow: auto;
  }

  div.container1 {
    display: inline-block;
  }

  div.upload{
      position: relative;
      left:150px;
      display: inline-block;
      margin: 10px;
      padding: 10px;
      border: #DCDCDC solid thin;
      background-color: #fdffff;
      border-radius: 30px;
      text-align: center;
      height: 650px;
      width: 500px;
  }

  div.upload_pic_txt {
    margin-top: 40px;
  }

  div.upload p {
      color:#808080;
      text-align:left;
      margin-left: 60px;
      margin-right: 60px;
      font-size: 15px;
      line-height: 20px;

  }
  div.upload h1 {
      text-align:left;
      margin-left: 60px;
  }

  div.upload input{
      height: 30px;
      border-style: none none solid none;
      border-color: #DCDCDC;
      font-size: 15px
  }

  div.upload #input1{
      width:300px;
      position: relative;
      right:40px;
      top: 0px;
  }

  div.upload #input2{
      width:300px;
      position: relative;
      right: 40px;
      top: 10px;
  }

  /* div.upload #btn1{
      width: 30px;
      height: 30px;
      position: relative;
      left:140px;
      bottom:25px;
      background-color: #fdffff;
      border:0px;
      cursor: pointer;
      opacity:1;
      background: url("/../assets/资源 3.png")
  } */

  div.upload_form img{
      position: relative;
      left:160px;
      bottom:25px;
  }

  div.upload #btn2{
      height: 25px;
      border-radius: 15px;
      background:#fdffff;
      border: solid 2px #969494;
      position: relative;
      right: 45px;
      top: 15px;
      cursor: pointer;
  }

  div.send {
    margin-left: 100px;
    width: 600px;
    display: inline-block;
    margin: 10px;
    padding: 10px;
    border: #DCDCDC solid thin;
    background-color: #fdffff;
    border-radius: 30px;
    text-align: center;
    position: absolute;
    left: 750px;
    height: 650px;
    top: 100px;
    width: 400px;
  }

  div.send #pic4{
      position: relative;
      left: 130px;
      bottom: 10px;
      height: 60px;
      width: 160px;
  }

  div.send #input3{
      width: 300px;
      height: 30px;
      font-size: 15px;
      border: none;
  }

  div.send #text1{
      position: relative;
      top:20px;
      width:350px;
      border:none;
      height: 500px;
      font-size: 15px;
  }

  div.send #line1 {
      width: 420px;
      height: 1px;
      border-top: solid #DCDCDC 1px;
      position: relative;
      top: 40px;
      right: 10px;
  }

</style>
