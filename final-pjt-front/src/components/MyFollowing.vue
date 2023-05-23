<template>
  <div>
    <h3>나의 팔로잉</h3>
    <ul>
      <li v-for="follower in followers" :key="follower.id">
        {{ follower.username }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyFollowers',
  data() {
    return {
      followers: []
    }
  },
  created() {
    this.getFollowers()
  },
  methods: {
    getFollowers() {
      axios({
        method: 'GET',
        url: '/api/user/followers/'  // 팔로우 리스트를 받아올 API 엔드포인트 설정
      })
        .then((response) => {
          this.followers = response.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }
}
</script>
