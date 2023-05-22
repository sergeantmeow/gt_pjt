<template>
  <div id="topEle">
    <div id="searchByArea">
      지역명으로 검색하기: <input type="text" placeholder="장소를 넣으세요" @keyup.enter="searchCinema">
    </div>
    또는
    <button class="btn_search_cinema">
      <div @click="loadNearCinema">
        근처영화관 조회하기
      </div>
    </button>
    <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' @click="showPlace(rs)" style="cursor: pointer">
      <div class="cinemaCard">
        <h5>{{ rs.place_name }}</h5>
      </div>
    </div>
    <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' 
    @click="showPlace2(rs)" 
    style="cursor: pointer">
      <div class="cinemaCard">
        <h5>{{ rs.name }}</h5>
      </div>  
    </div>
    <div id="kmap" class="kmap" ref="map">
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      cinemaList : null,
      options : {
        center: {
          lat: this.$store.state.userGEO[0],
          lng: this.$store.state.userGEO[1],
        },
        level: 4,
      }
    }
  },
  mounted(){
    console.log(this.options.center)
    this.renderMap()
    this.nearbyCinema()
  },
  
  methods : {
    renderMap(){
      let kakao = window.kakao;
      const container = this.$refs.map
      // 33.450701, 126.570667
      const {center, level} = this.options
      const mapInstance = new kakao.maps.Map(container, {
        center: new kakao.maps.LatLng(center.lat, center.lng),
        level,
      }); 
      console.log(mapInstance)
    },

    nearbyCinema(){
      this.$store.dispatch('getCinemas')
    },

    loadNearCinema(){
      this.cinemaList = this.$store.state.cinemaList
    },

    searchCinema(e){
      const keyword = `${e.target.value} 영화관`
      const ps = new window.kakao.maps.services.Places()  
      ps.keywordSearch(keyword, (data, status, pgn)=>{
        console.log(data)
        console.log(status)
        console.log(pgn)
        this.cinemaList = data
      })
    },

    showPlace(place){
      let kakao = window.kakao
      let X = place.x
      let Y = place.y
      const container = document.querySelector('.kmap')
      const mapInstance = new kakao.maps.Map(container, {
          center: new kakao.maps.LatLng(Y, X),
          level: 4,
        });

      //  set marker position 
      let markerPosition = new kakao.maps.LatLng(Y, X)

      // create instance of a marker
      let marker = new kakao.maps.Marker({
        position: markerPosition,
        clickable: true
      })

      // show marker on map
      marker.setMap(mapInstance)

      // create infoWindow
      let iwContent = 
        '<div id="infoBox" style="padding:5px"><div>'+place.place_name+'<br><a href="'+place.place_url+'" target="_blank" class="text-decoration-none">더보기</a></div></div>',
          iwRemoveable = true // to close infoWindow

      let infowindow = new kakao.maps.InfoWindow({
        content : iwContent,
        removable: iwRemoveable
      })

      // set clickevent on the marker
      kakao.maps.event.addListener(marker, 'click', function(){
        infowindow.open(mapInstance, marker)
      })
      console.log(place)
    },


    showPlace2(place){
      let kakao = window.kakao
      let geocoder = new kakao.maps.services.Geocoder(),
        wtmX = place.cood_x,
        wtmY = place.cood_y

      geocoder.transCoord(wtmX, wtmY, transCoordCB,{
        input_coord: kakao.maps.services.Coords.WTM,
        output_coord: kakao.maps.services.Coords.WGS84
      })
      const container = this.$refs.map
        
      function transCoordCB(result, status){
        const mapInstance = new kakao.maps.Map(container, {
          center: new kakao.maps.LatLng(result[0].y+0.003, result[0].x+0.0011),
          level: 5,
        }); 
        if(status === kakao.maps.services.Status.OK){
          let marker = new kakao.maps.Marker({
            position: new kakao.maps.LatLng(result[0].y+0.003, result[0].x+0.0011),
            map: mapInstance,
            clickable: true,
          })
          console.log(marker)
          let iwContent = 
            '<div style="padding:5px"><div>'+place.place_name+'<br><a href="'+place.place_url+'" target="_blank" class="text-decoration-none">더보기</a></div></div>',
              iwRemoveable = true // to close infoWindow

          let infowindow = new kakao.maps.InfoWindow({
            content : iwContent,
            removable: iwRemoveable
          })
          //////////////////////////////// 수정필 /////////////////////////////////
          // set clickevent on the marker
          kakao.maps.event.addListener(marker, 'click', function(){
            infowindow.open(mapInstance, marker)
          })
          console.log(place)
        }
      }
    },
  }
}
</script>

<style scoped>
  .kmap{
    width: 60%;
    height: 400px;
    margin: auto
  }

  #infoBox{
    text-align: center;
  }

  .btn_search_cinema{
    background-color: #261639;
    color: #ff2679;
    font-weight: bold;
    border: transparent;
    border-radius: 6px;
    margin-bottom: 10px;
  }
  .btn_search_cinema:hover{
    background-color: #352c41;
    color: #ff9ec3;
    font-weight: bold;
    border: transparent;
    border-radius: 6px;
    margin-bottom: 10px;
  }

  #searchByArea{
    margin-bottom: 10px;
  }
  
</style>