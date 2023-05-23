<template>
  <div>
    <h3 @click="toggleFollowings">팔로잉</h3>
    <ul v-if="showFollowings">
      <li v-for="following in followings" :key="following.id">
        <router-link :to="{ name: 'OtherProfileView', params: { username: following.username } }">
          {{ following.username }}
        </router-link>   
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'UserFollowings',
  data() {
    return {
      followings: [],
      showFollowings: false,
    }
  },
  props: {
    id: Number,
  },
  methods: {
    toggleFollowings() {
      if (this.showFollowings) {
        this.showFollowings = false;
      } else {
        this.getFollowings();
      }
    },
    getFollowings() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/${this.id}/followings/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        }
      })
      .then((response) => {
        this.followings = response.data;
        this.showFollowings = true;
      })
      .catch((error) => {
        console.error(error);
      });
    }
  }
}
</script>

<style scoped>

</style>