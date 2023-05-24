<template>
  <div>
    <h3 @click="toggleFollowings" class="following-title">팔로잉</h3>
    <ul v-if="showFollowings" class="list-group">
      <li v-for="following in followings" :key="following.id" class="list-group-item">
        <router-link :to="{ name: 'OtherProfileView',
         params: { username: following.username } }"
          class="item">
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
.following-title {
  transition: transform 0.3s ease;
}
.following-title:hover {
  transform: scale(1.1);
}

.list-group-item {
  border-color: rgb(31, 32, 63, 0);
  background-color: rgb(31, 32, 63, 0);
  color: #bfbfbf;
}

.list-group-item:hover {
  background-color: rgba(79, 61, 99, 0);
  color: #ff2679;
}

.item {
  color: #bfbfbf;
  text-decoration : none;
}

.item:hover {
  color: #ff2679
}
</style>