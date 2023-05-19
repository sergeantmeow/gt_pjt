<template>
  <div>
    <h2>TEST - KAKAOMAP 영화관들</h2>
    지역명으로 검색하기: <input type="text" placeholder="장소를 넣으세요" @keyup.enter="searchCinema">
    <div class="kmap" ref="map">
    </div>
      <div class="cinemas" v-for="rs in cinemaList" :key='rs.id' @click="showPlace(rs)">
        <h4>{{ rs.place_name }}</h4>
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
          lat: null,
          lng: null,
        },
        level: null
      }
    }
  },
  mounted(){
    if("geolocation" in navigator){
      console.log('>>>>>>>GEO data<<<<<<<<')
      navigator.geolocation.getCurrentPosition((position)=>{
        this.options.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        }
        this.options.level = 4
        this.renderMap()
      })
      
    }else{
      console.log('>>>>>>GEO data does not work<<<<<<<')
    }

    
    this.renderMap()
    // this.searchCinema()
  },
  
  methods : {
    renderMap(){
      let kakao = window.kakao;
    // console.log(this.$refs.map)
    const container = this.$refs.map
    // let options = {
    //   center: new kakao.maps.LatLng(33.450701, 126.570667),
    //   level: 3,
    // };
    const {center, level} = this.options
    const mapInstance = new kakao.maps.Map(container, {
      center: new kakao.maps.LatLng(center.lat, center.lng),
      level,
    }); 
    console.log(mapInstance)
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
      // let kakao = window.kakao
      // let markers = []
      // let ps = new kakao.maps.services.Places()
      // let infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
      // searchPlaces()

      // function searchPlaces(){
      //   let keyword = '영화관'
      //   ps.keywordSearch(keyword, placesSearchCB)
      // }
      // function placesSearchCB(data, status, pagination){
      //   if(status === kakao.maps.services.Status.OK){
      //     displayPlaces(data)
      //     displayPagination(pagination)
      //   }else if(status === kakao.maps.services.Status.ZERO_RESULT){
      //     alert('검색결과가 존재하지 않습니다')
      //   }else if(status === kakao.maps.services.Status.ERROR){
      //     alert('검색 중 오류가 발생하였습니다')
      //   }
      // }

      // function displayPlaces(places){
      //   let fragment = document.createDocumentFragment()
      //   let bounds = new kakao.maps.LatLngBounds()
      //   removeMarker()

      //   for(let i=0; i< places.length; i++){
      //     let placePosition = new kakao.maps.LatLng(places[i].y, places[i].x)
      //     let market = addMarker(placePosition, i)
      //     let itemEl = getListItem(i, places[i])

      //     bounds.extend(placePosition)

      //     (function(marker, title){
      //       kakao.maps.event.addListener(marker, 'mouseover', function(){
      //         displayInfowindow(marker, title)
      //       })
      //       kakao.maps.event.addListener(marker, 'mouseout', function(){
      //         infowindow.close()
      //       })
      //       itemEl.onmouseover = function(){
      //         displayInfowindow(marker, title)
      //       }
      //       itemEl.onmouseout = function(){
      //         infowindow.close()
      //       }
      //     })(marker, places[i].place_name)
      //     fragment.appendChild(itemEl)
      //   }
      //   mapInstance.setBounds(bounds)
      // }

    },
    showPlace(place){
      this.options.center = {
        lat: place.y,
        lng: place.x,
      }
      this.options.level = 3
      this.renderMap()
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
</style>