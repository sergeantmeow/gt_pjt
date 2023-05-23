<template>
  <div>
    <h3 @click="toggleFollowers">팔로워</h3>
    <ul v-if="showFollowers">
      <li v-for="follower in followers" :key="follower.id">
        <router-link :to="{ name: 'OtherProfileView', params: { username: follower.username } }">
          {{ follower.username }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'UserFollowers',
  data() {
    return {
      followers: [],
      showFollowers: false,
    }
  },
  props: {
    id: Number,
  },
  created() {
    this.getFollowers();
  },
  methods: {
    toggleFollowers() {
      if (this.showFollowers) {
        this.showFollowers = false;
      } else {
        this.getFollowers();
      }
    },
    getFollowers() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/${this.id}/followers/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        }
      })
      .then((response) => {
        this.followers = response.data;
        this.showFollowers = true;
      })
      .catch((error) => {
        console.error(error);
      });
    }
  },
}
</script>
