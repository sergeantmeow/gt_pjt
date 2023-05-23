<template>
  <div id="topEle">
    <div id="kmap" class="kmap" ref="map">
    </div>
    <div id="searchByArea">
      지역명으로 검색하기: <input type="text" id="areaSearch" placeholder="장소를 넣으세요" @keyup.enter="searchCinema">
    </div>
    또는
    <button class="btn_search_cinema">
      <div @click="loadNearCinema">
        근처영화관 조회하기
      </div>
    </button>
    <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' @click="showPlace(rs)" style="cursor: pointer">
      <div class="cinemaCard" v-if="searchMethod === 1">
        <h5>{{ rs.place_name }}</h5>
        <div id="cinemaInfo">
          <div>
            <h6>주소: {{ rs.road_address_name }}</h6>
          </div> 
          <div>
            <h6>연락처: {{ rs.phone }}</h6>
          </div>
        </div>
      </div>
    </div>
    <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' 
    @click="showPlace2(rs)" 
    style="cursor: pointer">
      <div class="cinemaCard2" v-if="searchMethod === 2">
        <h5>{{ rs.name }}</h5>
        <div id="cinemaInfo">
          <div>
            <h6>주소: {{ rs.address}}</h6>
          </div>
          <div>
            <h6>연락처: {{ rs.contact }}</h6>
          </div>
        </div>
      </div>  
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
      },
      searchMethod : 1,
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
      this.searchMethod = 2
      this.cinemaList = this.$store.state.cinemaList
    },

    searchCinema(e){
      this.searchMethod = 1
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


      // let overlayContent = '<div class="label"><span class="left"></span><span class="center">YEAH</span><span class="right"></span></div>'
      // let overlayPosition = new kakao.maps.LatLng(Y, X)
      // let customOverlay = new kakao.maps.CustomOverlay({
      //   position: overlayPosition,
      //   content: overlayContent,
      // })
      // kakao.maps.event.addListener(marker, 'click', function(){
      //   customOverlay.setMap(mapInstance)
      // })

      // create infoWindow
      let iwContent = 
        '<div id="infoBox" style="padding:5px; height: 100px; width: 300px; color: #ff2679; border-radius: 5px; background-color: #261639">' +
        ' <div>'+place.place_name+'<br>'+place.road_address_name+'<br>'+place.phone+'<br>' +
        '<a href="'+place.place_url+'" target="_blank" class="text-decoration-none">더보기</a></div></div>',
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
      const placeOb = place
        
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
          let iwContent = 
            '<div id="infoBox" style="padding:5px; height: 100px; width: 300px; color: #ff2679; border-radius: 5px; background-color: #261639">' +
            ' <div>'+placeOb.name+'<br>'+place.address+'<br>'+place.contact+'<br>' +
            // '<a href="'+place.place_url+'" target="_blank" class="text-decoration-none">더보기</a>' + 
            '</div></div>',
              iwRemoveable = true // to close infoWindow

          let infowindow = new kakao.maps.InfoWindow({
            content : iwContent,
            removable: iwRemoveable
          })
          
          // set clickevent on the marker
          kakao.maps.event.addListener(marker, 'click', function(){
            infowindow.open(mapInstance, marker)
          })
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

  #kmap{
    border : solid 2px #ff2679;
    border-radius: 4px;
    margin-bottom: 10px;
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

  #areaSearch{
    border : solid 2px #ff2679;
    border-radius: 4px;
    background-color: #261639;
    color: white;
    outline: none;
  }
  
  .cinemaCard{
    margin-bottom: 15px;
  }
  .cinemaCard2{
    margin-bottom: 15px;
  }
  
</style>