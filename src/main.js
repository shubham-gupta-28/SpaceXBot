import Vue from 'vue';
import Vuex from 'vuex';
import Vuetify from 'vuetify';
import {
  Config as AWSConfig,
  CognitoIdentityCredentials
} from 'aws-sdk/global';
import LexRuntime from 'aws-sdk/clients/lexruntime';
import Polly from 'aws-sdk/clients/polly';
import 'roboto-fontface/css/roboto/roboto-fontface.css';
import 'material-design-icons/iconfont/material-icons.css';
import 'vuetify/dist/vuetify.min.css';
import 'aws-lex-web-ui/dist/lex-web-ui.css';
import {
  Plugin as LexWebUi,
  Store as LexWebUiStore
} from 'aws-lex-web-ui/dist/lex-web-ui';

Vue.use(Vuex);
Vue.use(Vuetify);

const poolId = 'eu-west-1:3de4a6cc-970f-4ed5-b723-272ed255b31d';
const region = 'eu-west-1';
const credentials = new CognitoIdentityCredentials(
  { IdentityPoolId: poolId },
  { region }
);
const awsConfig = new AWSConfig({ region, credentials });
const lexRuntimeClient = new LexRuntime(awsConfig);
const pollyClient = new Polly(awsConfig);

const store = new Vuex.Store(LexWebUiStore);

// see the configuration section for details about the config fields
const config = {
  cognito: { poolId },
  lex: {
    botName: 'SpaceXBot',
    botAlias: '$LATEST',
    initialText: '',
    initialSpeechInstruction:
      "Say 'Tell me about Rockets' or 'Tell me about Missions' or 'Tell me about Launches' to get started."
  },
  ui: {
    parentOrigin: '',
    toolbarTitle: 'SpaceX Bot',
    toolbarLogo: '',
    enableLogin: false,
    AllowSuperDangerousHTMLInMessage: true,
    shouldDisplayResponseCardTitle: true,
    pushInitialTextOnRestart: true,
    directFocusToBotInput: true
  }
};

Vue.use(LexWebUi, { config, awsConfig, lexRuntimeClient, pollyClient });

// instantiate Vue
const vm = new Vue({
  el: '#lex-web-ui',
  // vuex store is in the lexWebUi instance
  store,
  // you can use the global LexWebUi/<lex-web-ui> commponent in templates
  template: `
    <div id="lex-web-ui-app">
      <lex-web-ui
        v-on:updateLexState="onUpdateLexState"
      ></lex-web-ui>
    </div>`,
  methods: {
    onUpdateLexState(lexState) {
      // handle lex state change events
    }
  }
});
